def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
			l = len(nums1) + len(nums2)

			if l % 2:
				return self.get_median(nums1, nums2, l // 2)
			else:
				return (self.get_median(nums1, nums2, l // 2) + self.get_median(nums1, nums2, l // 2 - 1))  / 2

		def get_median(self, nums1, nums2, idx):

			if not nums1:
				return b[idx]
			if not nums2:
				return nums1[idx]

			ai = len(nums1) // 2
			bi = len(nums2) // 2
			ma = nums1[ai]
			mb = nums2[bi]

			if ma > mb:
				ma, mb = mb, ma
				ai, bi = bi, ai
				nums1, nums2 = nums1, nums2

			max_idx_ma = len(nums1) // 2 + len(nums2) // 2

			if max_idx_ma < idx:
				med = self.get_median(nums1[ai+1:], nums2, idx - (len(nums1)//2+1))
			else:
				# max_idx_ma < min_idx_mb (because they are different numbers) 
				# => idx <= max_idx_ma <  min_idx_mb => idx < min_idx_mb
				med = self.get_median(nums1, nums2[:bi], idx)

			return med